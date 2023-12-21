// Generated from c:/Users/User/OneDrive/Documenten/Open Universiteit/IB9902 Voorbereiden Afstuderen/sycococopy/antlrFiles/Pythonic.g4 by ANTLR 4.13.1

from antlr_denter.DenterHelper import DenterHelper
from PythonicParser import PythonicParser

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class PythonicLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROTOCOL=1, ROLES=2, TO=3, FROM=4, SEND=5, SEQUENCE=6, SHUFFLE=7, CHOICE=8, 
		REPEAT=9, LOOP=10, CLOSE=11, LOOPLABEL=12, OPENINGBRACKET=13, CLOSINGBRACKET=14, 
		COMMA=15, BOOLEAN=16, PRIMITIVE=17, INTEGER=18, STRING=19, FLOAT=20, COMPARATOR=21, 
		WORD=22, WS=23, NL=24;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", "CHOICE", 
			"REPEAT", "LOOP", "CLOSE", "LOOPLABEL", "OPENINGBRACKET", "CLOSINGBRACKET", 
			"COMMA", "BOOLEAN", "PRIMITIVE", "INTEGER", "STRING", "FLOAT", "COMPARATOR", 
			"WORD", "WS", "NL"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'protocol:'", "'roles:'", "'to'", "'from'", "'send'", "'sequence:'", 
			"'shuffle:'", "'choice:'", "'repeat'", "'loop'", "'close'", null, "'('", 
			"')'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
			"CHOICE", "REPEAT", "LOOP", "CLOSE", "LOOPLABEL", "OPENINGBRACKET", "CLOSINGBRACKET", 
			"COMMA", "BOOLEAN", "PRIMITIVE", "INTEGER", "STRING", "FLOAT", "COMPARATOR", 
			"WORD", "WS", "NL"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	class MyCoolDenter(DenterHelper):
	    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
	        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
	        self.lexer: PythonicLexer = lexer

	    def pull_token(self):
	        return super(PythonicLexer, self.lexer).nextToken()

	denter = None

	def nextToken(self):
	    if not self.denter:
	        self.denter = self.MyCoolDenter(self, self.NL, PythonicParser.INDENT, PythonicParser.DEDENT, False)
	    return self.denter.next_token()



	public PythonicLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Pythonic.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0018\u00e5\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0003\u000f\u008f\b\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0003\u0010\u0094\b\u0010\u0001\u0011\u0003\u0011\u0097\b\u0011"+
		"\u0001\u0011\u0001\u0011\u0005\u0011\u009b\b\u0011\n\u0011\f\u0011\u009e"+
		"\t\u0011\u0001\u0011\u0003\u0011\u00a1\b\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0005\u0012\u00a7\b\u0012\n\u0012\f\u0012\u00aa"+
		"\t\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0003\u0013\u00af\b\u0013"+
		"\u0001\u0013\u0004\u0013\u00b2\b\u0013\u000b\u0013\f\u0013\u00b3\u0001"+
		"\u0013\u0001\u0013\u0004\u0013\u00b8\b\u0013\u000b\u0013\f\u0013\u00b9"+
		"\u0001\u0013\u0003\u0013\u00bd\b\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0004\u0013\u00c2\b\u0013\u000b\u0013\f\u0013\u00c3\u0003\u0013\u00c6"+
		"\b\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u00d1\b\u0014\u0001"+
		"\u0015\u0004\u0015\u00d4\b\u0015\u000b\u0015\f\u0015\u00d5\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0003\u0017\u00dd\b\u0017"+
		"\u0001\u0017\u0001\u0017\u0005\u0017\u00e1\b\u0017\n\u0017\f\u0017\u00e4"+
		"\t\u0017\u0001\u00a8\u0000\u0018\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b"+
		"\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013"+
		"\'\u0014)\u0015+\u0016-\u0017/\u0018\u0001\u0000\u0006\u0001\u0000--\u0001"+
		"\u000019\u0001\u000009\u0001\u000000\u0002\u0000<<>>\u0004\u000009AZ_"+
		"_az\u00f9\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00011\u0001\u0000\u0000\u0000\u0003"+
		";\u0001\u0000\u0000\u0000\u0005B\u0001\u0000\u0000\u0000\u0007E\u0001"+
		"\u0000\u0000\u0000\tJ\u0001\u0000\u0000\u0000\u000bO\u0001\u0000\u0000"+
		"\u0000\rY\u0001\u0000\u0000\u0000\u000fb\u0001\u0000\u0000\u0000\u0011"+
		"j\u0001\u0000\u0000\u0000\u0013q\u0001\u0000\u0000\u0000\u0015v\u0001"+
		"\u0000\u0000\u0000\u0017|\u0001\u0000\u0000\u0000\u0019\u007f\u0001\u0000"+
		"\u0000\u0000\u001b\u0081\u0001\u0000\u0000\u0000\u001d\u0083\u0001\u0000"+
		"\u0000\u0000\u001f\u008e\u0001\u0000\u0000\u0000!\u0093\u0001\u0000\u0000"+
		"\u0000#\u00a0\u0001\u0000\u0000\u0000%\u00a2\u0001\u0000\u0000\u0000\'"+
		"\u00c5\u0001\u0000\u0000\u0000)\u00d0\u0001\u0000\u0000\u0000+\u00d3\u0001"+
		"\u0000\u0000\u0000-\u00d7\u0001\u0000\u0000\u0000/\u00dc\u0001\u0000\u0000"+
		"\u000012\u0005p\u0000\u000023\u0005r\u0000\u000034\u0005o\u0000\u0000"+
		"45\u0005t\u0000\u000056\u0005o\u0000\u000067\u0005c\u0000\u000078\u0005"+
		"o\u0000\u000089\u0005l\u0000\u00009:\u0005:\u0000\u0000:\u0002\u0001\u0000"+
		"\u0000\u0000;<\u0005r\u0000\u0000<=\u0005o\u0000\u0000=>\u0005l\u0000"+
		"\u0000>?\u0005e\u0000\u0000?@\u0005s\u0000\u0000@A\u0005:\u0000\u0000"+
		"A\u0004\u0001\u0000\u0000\u0000BC\u0005t\u0000\u0000CD\u0005o\u0000\u0000"+
		"D\u0006\u0001\u0000\u0000\u0000EF\u0005f\u0000\u0000FG\u0005r\u0000\u0000"+
		"GH\u0005o\u0000\u0000HI\u0005m\u0000\u0000I\b\u0001\u0000\u0000\u0000"+
		"JK\u0005s\u0000\u0000KL\u0005e\u0000\u0000LM\u0005n\u0000\u0000MN\u0005"+
		"d\u0000\u0000N\n\u0001\u0000\u0000\u0000OP\u0005s\u0000\u0000PQ\u0005"+
		"e\u0000\u0000QR\u0005q\u0000\u0000RS\u0005u\u0000\u0000ST\u0005e\u0000"+
		"\u0000TU\u0005n\u0000\u0000UV\u0005c\u0000\u0000VW\u0005e\u0000\u0000"+
		"WX\u0005:\u0000\u0000X\f\u0001\u0000\u0000\u0000YZ\u0005s\u0000\u0000"+
		"Z[\u0005h\u0000\u0000[\\\u0005u\u0000\u0000\\]\u0005f\u0000\u0000]^\u0005"+
		"f\u0000\u0000^_\u0005l\u0000\u0000_`\u0005e\u0000\u0000`a\u0005:\u0000"+
		"\u0000a\u000e\u0001\u0000\u0000\u0000bc\u0005c\u0000\u0000cd\u0005h\u0000"+
		"\u0000de\u0005o\u0000\u0000ef\u0005i\u0000\u0000fg\u0005c\u0000\u0000"+
		"gh\u0005e\u0000\u0000hi\u0005:\u0000\u0000i\u0010\u0001\u0000\u0000\u0000"+
		"jk\u0005r\u0000\u0000kl\u0005e\u0000\u0000lm\u0005p\u0000\u0000mn\u0005"+
		"e\u0000\u0000no\u0005a\u0000\u0000op\u0005t\u0000\u0000p\u0012\u0001\u0000"+
		"\u0000\u0000qr\u0005l\u0000\u0000rs\u0005o\u0000\u0000st\u0005o\u0000"+
		"\u0000tu\u0005p\u0000\u0000u\u0014\u0001\u0000\u0000\u0000vw\u0005c\u0000"+
		"\u0000wx\u0005l\u0000\u0000xy\u0005o\u0000\u0000yz\u0005s\u0000\u0000"+
		"z{\u0005e\u0000\u0000{\u0016\u0001\u0000\u0000\u0000|}\u0003+\u0015\u0000"+
		"}~\u0005:\u0000\u0000~\u0018\u0001\u0000\u0000\u0000\u007f\u0080\u0005"+
		"(\u0000\u0000\u0080\u001a\u0001\u0000\u0000\u0000\u0081\u0082\u0005)\u0000"+
		"\u0000\u0082\u001c\u0001\u0000\u0000\u0000\u0083\u0084\u0005,\u0000\u0000"+
		"\u0084\u001e\u0001\u0000\u0000\u0000\u0085\u0086\u0005T\u0000\u0000\u0086"+
		"\u0087\u0005r\u0000\u0000\u0087\u0088\u0005u\u0000\u0000\u0088\u008f\u0005"+
		"e\u0000\u0000\u0089\u008a\u0005F\u0000\u0000\u008a\u008b\u0005a\u0000"+
		"\u0000\u008b\u008c\u0005l\u0000\u0000\u008c\u008d\u0005s\u0000\u0000\u008d"+
		"\u008f\u0005e\u0000\u0000\u008e\u0085\u0001\u0000\u0000\u0000\u008e\u0089"+
		"\u0001\u0000\u0000\u0000\u008f \u0001\u0000\u0000\u0000\u0090\u0094\u0003"+
		"%\u0012\u0000\u0091\u0094\u0003#\u0011\u0000\u0092\u0094\u0003\'\u0013"+
		"\u0000\u0093\u0090\u0001\u0000\u0000\u0000\u0093\u0091\u0001\u0000\u0000"+
		"\u0000\u0093\u0092\u0001\u0000\u0000\u0000\u0094\"\u0001\u0000\u0000\u0000"+
		"\u0095\u0097\u0007\u0000\u0000\u0000\u0096\u0095\u0001\u0000\u0000\u0000"+
		"\u0096\u0097\u0001\u0000\u0000\u0000\u0097\u0098\u0001\u0000\u0000\u0000"+
		"\u0098\u009c\u0007\u0001\u0000\u0000\u0099\u009b\u0007\u0002\u0000\u0000"+
		"\u009a\u0099\u0001\u0000\u0000\u0000\u009b\u009e\u0001\u0000\u0000\u0000"+
		"\u009c\u009a\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000"+
		"\u009d\u00a1\u0001\u0000\u0000\u0000\u009e\u009c\u0001\u0000\u0000\u0000"+
		"\u009f\u00a1\u0007\u0003\u0000\u0000\u00a0\u0096\u0001\u0000\u0000\u0000"+
		"\u00a0\u009f\u0001\u0000\u0000\u0000\u00a1$\u0001\u0000\u0000\u0000\u00a2"+
		"\u00a8\u0005\"\u0000\u0000\u00a3\u00a4\u0005\\\u0000\u0000\u00a4\u00a7"+
		"\u0005\"\u0000\u0000\u00a5\u00a7\t\u0000\u0000\u0000\u00a6\u00a3\u0001"+
		"\u0000\u0000\u0000\u00a6\u00a5\u0001\u0000\u0000\u0000\u00a7\u00aa\u0001"+
		"\u0000\u0000\u0000\u00a8\u00a9\u0001\u0000\u0000\u0000\u00a8\u00a6\u0001"+
		"\u0000\u0000\u0000\u00a9\u00ab\u0001\u0000\u0000\u0000\u00aa\u00a8\u0001"+
		"\u0000\u0000\u0000\u00ab\u00ac\u0005\"\u0000\u0000\u00ac&\u0001\u0000"+
		"\u0000\u0000\u00ad\u00af\u0007\u0000\u0000\u0000\u00ae\u00ad\u0001\u0000"+
		"\u0000\u0000\u00ae\u00af\u0001\u0000\u0000\u0000\u00af\u00b1\u0001\u0000"+
		"\u0000\u0000\u00b0\u00b2\u0007\u0001\u0000\u0000\u00b1\u00b0\u0001\u0000"+
		"\u0000\u0000\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3\u00b1\u0001\u0000"+
		"\u0000\u0000\u00b3\u00b4\u0001\u0000\u0000\u0000\u00b4\u00b5\u0001\u0000"+
		"\u0000\u0000\u00b5\u00b7\u0005.\u0000\u0000\u00b6\u00b8\u0007\u0002\u0000"+
		"\u0000\u00b7\u00b6\u0001\u0000\u0000\u0000\u00b8\u00b9\u0001\u0000\u0000"+
		"\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00b9\u00ba\u0001\u0000\u0000"+
		"\u0000\u00ba\u00c6\u0001\u0000\u0000\u0000\u00bb\u00bd\u0007\u0000\u0000"+
		"\u0000\u00bc\u00bb\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001\u0000\u0000"+
		"\u0000\u00bd\u00be\u0001\u0000\u0000\u0000\u00be\u00bf\u0007\u0003\u0000"+
		"\u0000\u00bf\u00c1\u0005.\u0000\u0000\u00c0\u00c2\u0007\u0002\u0000\u0000"+
		"\u00c1\u00c0\u0001\u0000\u0000\u0000\u00c2\u00c3\u0001\u0000\u0000\u0000"+
		"\u00c3\u00c1\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000\u0000\u0000"+
		"\u00c4\u00c6\u0001\u0000\u0000\u0000\u00c5\u00ae\u0001\u0000\u0000\u0000"+
		"\u00c5\u00bc\u0001\u0000\u0000\u0000\u00c6(\u0001\u0000\u0000\u0000\u00c7"+
		"\u00d1\u0007\u0004\u0000\u0000\u00c8\u00c9\u0005<\u0000\u0000\u00c9\u00d1"+
		"\u0005=\u0000\u0000\u00ca\u00cb\u0005>\u0000\u0000\u00cb\u00d1\u0005="+
		"\u0000\u0000\u00cc\u00cd\u0005!\u0000\u0000\u00cd\u00d1\u0005=\u0000\u0000"+
		"\u00ce\u00cf\u0005=\u0000\u0000\u00cf\u00d1\u0005=\u0000\u0000\u00d0\u00c7"+
		"\u0001\u0000\u0000\u0000\u00d0\u00c8\u0001\u0000\u0000\u0000\u00d0\u00ca"+
		"\u0001\u0000\u0000\u0000\u00d0\u00cc\u0001\u0000\u0000\u0000\u00d0\u00ce"+
		"\u0001\u0000\u0000\u0000\u00d1*\u0001\u0000\u0000\u0000\u00d2\u00d4\u0007"+
		"\u0005\u0000\u0000\u00d3\u00d2\u0001\u0000\u0000\u0000\u00d4\u00d5\u0001"+
		"\u0000\u0000\u0000\u00d5\u00d3\u0001\u0000\u0000\u0000\u00d5\u00d6\u0001"+
		"\u0000\u0000\u0000\u00d6,\u0001\u0000\u0000\u0000\u00d7\u00d8\u0005 \u0000"+
		"\u0000\u00d8\u00d9\u0001\u0000\u0000\u0000\u00d9\u00da\u0006\u0016\u0000"+
		"\u0000\u00da.\u0001\u0000\u0000\u0000\u00db\u00dd\u0005\r\u0000\u0000"+
		"\u00dc\u00db\u0001\u0000\u0000\u0000\u00dc\u00dd\u0001\u0000\u0000\u0000"+
		"\u00dd\u00de\u0001\u0000\u0000\u0000\u00de\u00e2\u0005\n\u0000\u0000\u00df"+
		"\u00e1\u0005 \u0000\u0000\u00e0\u00df\u0001\u0000\u0000\u0000\u00e1\u00e4"+
		"\u0001\u0000\u0000\u0000\u00e2\u00e0\u0001\u0000\u0000\u0000\u00e2\u00e3"+
		"\u0001\u0000\u0000\u0000\u00e30\u0001\u0000\u0000\u0000\u00e4\u00e2\u0001"+
		"\u0000\u0000\u0000\u0013\u0000\u008e\u0093\u0096\u009c\u00a0\u00a6\u00a8"+
		"\u00ae\u00b3\u00b9\u00bc\u00c3\u00c5\u00d0\u00d3\u00d5\u00dc\u00e2\u0001"+
		"\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}