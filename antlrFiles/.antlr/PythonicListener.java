// Generated from c:/Users/User/OneDrive/Documenten/Open Universiteit/IB9902 Voorbereiden Afstuderen/sycococopy/antlrFiles/Pythonic.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PythonicParser}.
 */
public interface PythonicListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PythonicParser#specification}.
	 * @param ctx the parse tree
	 */
	void enterSpecification(PythonicParser.SpecificationContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#specification}.
	 * @param ctx the parse tree
	 */
	void exitSpecification(PythonicParser.SpecificationContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#protocol}.
	 * @param ctx the parse tree
	 */
	void enterProtocol(PythonicParser.ProtocolContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#protocol}.
	 * @param ctx the parse tree
	 */
	void exitProtocol(PythonicParser.ProtocolContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(PythonicParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(PythonicParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#sequence}.
	 * @param ctx the parse tree
	 */
	void enterSequence(PythonicParser.SequenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#sequence}.
	 * @param ctx the parse tree
	 */
	void exitSequence(PythonicParser.SequenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#shuffle}.
	 * @param ctx the parse tree
	 */
	void enterShuffle(PythonicParser.ShuffleContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#shuffle}.
	 * @param ctx the parse tree
	 */
	void exitShuffle(PythonicParser.ShuffleContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#choice}.
	 * @param ctx the parse tree
	 */
	void enterChoice(PythonicParser.ChoiceContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#choice}.
	 * @param ctx the parse tree
	 */
	void exitChoice(PythonicParser.ChoiceContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#loop}.
	 * @param ctx the parse tree
	 */
	void enterLoop(PythonicParser.LoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#loop}.
	 * @param ctx the parse tree
	 */
	void exitLoop(PythonicParser.LoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#repeat}.
	 * @param ctx the parse tree
	 */
	void enterRepeat(PythonicParser.RepeatContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#repeat}.
	 * @param ctx the parse tree
	 */
	void exitRepeat(PythonicParser.RepeatContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#send}.
	 * @param ctx the parse tree
	 */
	void enterSend(PythonicParser.SendContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#send}.
	 * @param ctx the parse tree
	 */
	void exitSend(PythonicParser.SendContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#close}.
	 * @param ctx the parse tree
	 */
	void enterClose(PythonicParser.CloseContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#close}.
	 * @param ctx the parse tree
	 */
	void exitClose(PythonicParser.CloseContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(PythonicParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(PythonicParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#roles}.
	 * @param ctx the parse tree
	 */
	void enterRoles(PythonicParser.RolesContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#roles}.
	 * @param ctx the parse tree
	 */
	void exitRoles(PythonicParser.RolesContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#roleblock}.
	 * @param ctx the parse tree
	 */
	void enterRoleblock(PythonicParser.RoleblockContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#roleblock}.
	 * @param ctx the parse tree
	 */
	void exitRoleblock(PythonicParser.RoleblockContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonicParser#role}.
	 * @param ctx the parse tree
	 */
	void enterRole(PythonicParser.RoleContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonicParser#role}.
	 * @param ctx the parse tree
	 */
	void exitRole(PythonicParser.RoleContext ctx);
}